import { Mark } from 'vega-lite/build/src/mark';
import { QueryConfig } from '../../config';
import { SpecQueryModel } from '../../model';
import { Schema } from '../../schema';
import { Dict } from '../../util';
import { FeatureScore } from '../ranking';
import { Scorer } from './base';
import { ExtendedType } from './type';
export declare class MarkScorer extends Scorer {
    constructor();
    protected initScore(): Dict<number>;
    getScore(specM: SpecQueryModel, _: Schema, __: QueryConfig): FeatureScore[];
}
export declare function featurize(xType: ExtendedType, yType: ExtendedType, hasOcclusion: boolean, mark: Mark): string;
