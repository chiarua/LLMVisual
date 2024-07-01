import { QueryConfig } from '../../config';
import { SpecQueryModel } from '../../model';
import { Schema } from '../../schema';
import { Dict } from '../../util';
import { FeatureScore } from '../ranking';
import { Scorer } from './base';
/**
 * Effective Score for preferred facet
 */
export declare class FacetScorer extends Scorer {
    constructor();
    protected initScore(opt?: QueryConfig): Dict<number>;
    getScore(specM: SpecQueryModel, _: Schema, __: QueryConfig): FeatureScore[];
}
